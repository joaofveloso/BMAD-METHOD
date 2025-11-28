#!/usr/bin/env python3
"""
Email Server Processing Functions
Core functions for IMAP, SMTP, and email management operations
"""

import imaplib
import smtplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import ssl
from datetime import datetime, timedelta
import subprocess

def connect_email_server(user_email, password):
    """Connect to the mail server using IMAP SSL"""
    context = ssl.create_default_context()
    imap = imaplib.IMAP4_SSL("mail.localdomain", 993, ssl_context=context)
    try:
        imap.login(user_email, password)
        return imap
    except Exception as e:
        print(f"Failed to connect: {e}")
        return None

def list_all_folders(imap):
    """List all available folders"""
    try:
        status, folders = imap.list()
        if status == 'OK':
            return [folder.decode().split('"')[-2] for folder in folders]
        return []
    except Exception as e:
        print(f"Error listing folders: {e}")
        return []

def create_folder(imap, folder_name):
    """Create a new folder"""
    try:
        status, response = imap.create(f'"{folder_name}"')
        return status == 'OK'
    except Exception as e:
        print(f"Error creating folder {folder_name}: {e}")
        return False

def move_email_to_folder(imap, email_uid, source_folder, target_folder):
    """Move an email to another folder"""
    try:
        imap.select(f'"{source_folder}"')
        status, response = imap.copy(email_uid, f'"{target_folder}"')
        if status == 'OK':
            imap.store(email_uid, '+FLAGS', '\\Deleted')
            imap.expunge()
            return True
        return False
    except Exception as e:
        print(f"Error moving email: {e}")
        return False

def get_folder_stats(imap, folder_name):
    """Get statistics for a folder"""
    try:
        imap.select(f'"{folder_name}"')
        status, data = imap.search(None, 'ALL')
        if status == 'OK':
            email_count = len(data[0].split())
            status, data = imap.uid('search', None, 'UNSEEN')
            unread_count = len(data[0].split()) if status == 'OK' else 0
            return {'total': email_count, 'unread': unread_count}
        return {'total': 0, 'unread': 0}
    except Exception as e:
        print(f"Error getting folder stats for {folder_name}: {e}")
        return {'total': 0, 'unread': 0}

def set_email_flags(imap, folder_name, email_uid, flags):
    """Set flags on an email (\\Seen, \\Flagged, \\Answered, \\Draft, \\Deleted)"""
    try:
        imap.select(f'"{folder_name}"')
        status, response = imap.store(email_uid, '+FLAGS', flags)
        return status == 'OK'
    except Exception as e:
        print(f"Error setting flags: {e}")
        return False

def remove_email_flags(imap, folder_name, email_uid, flags):
    """Remove flags from an email"""
    try:
        imap.select(f'"{folder_name}"')
        status, response = imap.store(email_uid, '-FLAGS', flags)
        return status == 'OK'
    except Exception as e:
        print(f"Error removing flags: {e}")
        return False

def mark_email_as_read(imap, folder_name, email_uid):
    """Mark email as read"""
    return set_email_flags(imap, folder_name, email_uid, '\\Seen')

def mark_email_as_important(imap, folder_name, email_uid):
    """Mark email as important (star it)"""
    return set_email_flags(imap, folder_name, email_uid, '\\Flagged')

def mark_email_as_answered(imap, folder_name, email_uid):
    """Mark email as answered"""
    return set_email_flags(imap, folder_name, email_uid, '\\Answered')

def find_flagged_emails(imap, folder_name):
    """Find all flagged/important emails"""
    try:
        imap.select(f'"{folder_name}"')
        status, data = imap.search(None, 'FLAGGED')
        if status == 'OK':
            return data[0].split()
        return []
    except Exception as e:
        print(f"Error finding flagged emails: {e}")
        return []

def send_email(sender_email, sender_password, recipient_email, subject, body,
               attachment_path=None, cc_emails=None, bcc_emails=None):
    """Send an email with optional attachments"""
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        if cc_emails:
            msg['Cc'] = ', '.join(cc_emails)
        if bcc_emails:
            msg['Bcc'] = ', '.join(bcc_emails)

        msg.attach(MIMEText(body, 'plain'))

        # Add attachment if provided
        if attachment_path:
            with open(attachment_path, "rb") as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())

            encoders.encode_base64(part)
            part.add_header(
                'Content-Disposition',
                f'attachment; filename= {attachment_path.split("/")[-1]}'
            )
            msg.attach(part)

        # Send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("mail.localdomain", 465, context=context) as server:
            server.login(sender_email, sender_password)
            text = msg.as_string()
            server.sendmail(sender_email, [recipient_email] + (cc_emails or []) + (bcc_emails or []), text)

        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

def send_html_email(sender_email, sender_password, recipient_email, subject, html_body):
    """Send HTML formatted email"""
    try:
        msg = MIMEMultipart('alternative')
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        html_part = MIMEText(html_body, 'html')
        msg.attach(html_part)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("mail.localdomain", 465, context=context) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, [recipient_email], msg.as_string())

        return True
    except Exception as e:
        print(f"Error sending HTML email: {e}")
        return False

def get_email_list(imap, folder_name, limit=10):
    """Get list of emails in a folder"""
    try:
        imap.select(f'"{folder_name}"')
        status, data = imap.search(None, 'ALL')
        if status != 'OK':
            return []

        email_ids = data[0].split()[-limit:]  # Get last N emails
        emails = []

        for email_id in email_ids:
            status, data = imap.fetch(email_id, '(RFC822)')
            if status == 'OK':
                raw_email = data[0][1]
                email_obj = email.message_from_bytes(raw_email)
                emails.append({
                    'id': email_id.decode(),
                    'subject': email_obj.get('Subject', 'No Subject'),
                    'from': email_obj.get('From', 'No Sender'),
                    'date': email_obj.get('Date', 'No Date'),
                    'body': email_obj
                })

        return emails
    except Exception as e:
        print(f"Error getting email list: {e}")
        return []

def get_email_body(imap, folder_name, email_id):
    """Get full email body"""
    try:
        imap.select(f'"{folder_name}"')
        status, data = imap.fetch(email_id, '(RFC822)')
        if status != 'OK':
            return None

        email_obj = email.message_from_bytes(data[0][1])
        body = ""

        if email_obj.is_multipart():
            for part in email_obj.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode()
                    break
        else:
            body = email_obj.get_payload(decode=True).decode()

        return body
    except Exception as e:
        print(f"Error getting email body: {e}")
        return None

def search_emails(imap, folder_name, search_criteria):
    """Search emails by criteria"""
    try:
        imap.select(f'"{folder_name}"')
        status, data = imap.search(None, search_criteria)
        if status == 'OK':
            return data[0].split()
        return []
    except Exception as e:
        print(f"Error searching emails: {e}")
        return []

def search_by_subject(imap, folder_name, subject_text):
    """Search emails by subject"""
    return search_emails(imap, folder_name, f'SUBJECT "{subject_text}"')

def search_by_sender(imap, folder_name, sender_email):
    """Search emails by sender"""
    return search_emails(imap, folder_name, f'FROM "{sender_email}"')

def archive_old_emails(imap, source_folder, archive_folder='Archive', days_old=30):
    """Archive emails older than specified days"""
    try:
        imap.select(f'"{source_folder}"')
        date_threshold = (datetime.now() - timedelta(days=days_old)).strftime("%d-%b-%Y")
        status, data = imap.search(None, f'BEFORE "{date_threshold}"')
        if status != 'OK':
            return 0

        email_ids = data[0].split()
        archived_count = 0

        for email_id in email_ids:
            if move_email_to_folder(imap, email_id.decode(), source_folder, archive_folder):
                archived_count += 1

        return archived_count
    except Exception as e:
        print(f"Error archiving emails: {e}")
        return 0

def empty_trash_folder(imap):
    """Permanently delete all emails in Trash"""
    try:
        imap.select('"Trash"')
        status, data = imap.search(None, 'ALL')
        if status == 'OK':
            email_ids = data[0].split()
            for email_id in email_ids:
                imap.store(email_id, '+FLAGS', '\\Deleted')
            imap.expunge()
            return len(email_ids)
        return 0
    except Exception as e:
        print(f"Error emptying trash: {e}")
        return 0

def get_email_statistics(imap):
    """Get comprehensive email statistics"""
    folders = list_all_folders(imap)
    stats = {}

    for folder in folders:
        try:
            folder_stats = get_folder_stats(imap, folder)
            stats[folder] = folder_stats
        except:
            stats[folder] = {'total': 0, 'unread': 0}

    return stats

def check_server_status():
    """Check mail server status"""
    try:
        # Check Dovecot
        dovecot_status = subprocess.run(['pgrep', 'dovecot'], capture_output=True)
        dovecot_running = dovecot_status.returncode == 0

        # Check Postfix
        postfix_status = subprocess.run(['pgrep', 'postfix'], capture_output=True)
        postfix_running = postfix_status.returncode == 0

        return {
            'dovecot': dovecot_running,
            'postfix': postfix_running,
            'timestamp': datetime.now().isoformat()
        }
    except Exception as e:
        return {'error': str(e), 'timestamp': datetime.now().isoformat()}

def check_mail_queue():
    """Check Postfix mail queue"""
    try:
        result = subprocess.run(['mailq'], capture_output=True, text=True)
        if 'Mail queue is empty' in result.stdout:
            return {'queue_size': 0, 'status': 'empty'}
        else:
            lines = result.stdout.strip().split('\n')
            queue_size = len([line for line in lines if line and not line.startswith('--')])
            return {'queue_size': queue_size, 'status': 'has_messages'}
    except Exception as e:
        return {'error': str(e)}

print("Email processor functions loaded successfully!")
