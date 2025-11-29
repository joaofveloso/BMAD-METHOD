#!/usr/bin/env python3
"""
Complete Email Management Automation Script
Usage: python email_manager.py [command] [options]
"""

import argparse
import json
import sys
import os
from datetime import datetime, timedelta

# Import our email processor functions
try:
    from email_processor import *
except ImportError:
    print("Error: email_processor.py not found. Make sure it's in the same directory.")
    sys.exit(1)

class EmailManager:
    def __init__(self, user_email, password):
        self.user_email = user_email
        self.password = password
        self.imap = None

    def connect(self):
        """Connect to email server"""
        print(f"Connecting to {self.user_email}...")
        self.imap = connect_email_server(self.user_email, self.password)
        if self.imap:
            print("Connected successfully!")
            return True
        else:
            print("Failed to connect to email server")
            return False

    def disconnect(self):
        """Disconnect from email server"""
        if self.imap:
            print("Disconnecting from email server...")
            self.imap.logout()
            print("Disconnected successfully!")

    def create_project_folder(self, project_name):
        """Create a project-specific folder"""
        folder_name = f"Projects-{project_name}"
        print(f"Creating folder: {folder_name}")

        if create_folder(self.imap, folder_name):
            print(f"Successfully created folder: {folder_name}")
            return True
        else:
            print(f"Failed to create folder: {folder_name}")
            return False

    def organize_project_emails(self, project_keywords, project_name):
        """Move emails with project keywords to project folder"""
        folder_name = f"Projects-{project_name}"
        print(f"Organizing emails for project: {project_name}")
        print(f"Keywords: {project_keywords}")

        total_moved = 0
        for keyword in project_keywords:
            print(f"   Searching for keyword: '{keyword}'...")
            emails = search_emails(self.imap, 'INBOX', f'SUBJECT "{keyword}"')
            print(f"   Found {len(emails)} emails with '{keyword}'")

            for email_id in emails:
                if move_email_to_folder(self.imap, email_id.decode(), 'INBOX', folder_name):
                    total_moved += 1

        print(f"Moved {total_moved} emails to {folder_name}")
        return total_moved

    def mark_emails_from_sender_as_important(self, sender_email):
        """Mark all emails from specific sender as important"""
        print(f"Marking emails from {sender_email} as important")

        emails = search_by_sender(self.imap, 'INBOX', sender_email)
        print(f"   Found {len(emails)} emails from {sender_email}")

        important_count = 0
        for email_id in emails:
            if mark_email_as_important(self.imap, 'INBOX', email_id.decode()):
                important_count += 1

        print(f"Marked {important_count} emails from {sender_email} as important")
        return important_count

    def email_digest(self):
        """Generate daily email digest"""
        print("Generating email digest...")

        stats = get_email_statistics(self.imap)

        digest = f"""
Email Digest for {self.user_email}
Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Folder Statistics:
"""

        total_emails = 0
        total_unread = 0

        for folder, data in stats.items():
            digest += f"  - {folder}: {data['total']} emails, {data['unread']} unread\n"
            total_emails += data['total']
            total_unread += data['unread']

        # Count important emails
        important_emails = find_flagged_emails(self.imap, 'INBOX')

        read_percentage = ((total_emails - total_unread) / total_emails * 100) if total_emails > 0 else 0

        digest += f"""
Summary:
  - Total emails: {total_emails}
  - Unread emails: {total_unread}
  - Read percentage: {read_percentage:.1f}%

Important emails: {len(important_emails)}
"""

        print(digest)
        return digest

    def cleanup_old_emails(self, days_threshold=90):
        """Clean up old emails across all folders"""
        print(f"Cleaning up emails older than {days_threshold} days...")

        total_archived = 0
        deleted = 0

        # Archive old emails from main folders
        main_folders = ['INBOX', 'Sent', 'Work', 'Projects']
        for folder in main_folders:
            print(f"   Processing folder: {folder}")
            try:
                archived = archive_old_emails(self.imap, folder, 'Archive', days_threshold)
                total_archived += archived
                print(f"   Archived {archived} emails from {folder}")
            except Exception as e:
                print(f"   Error processing {folder}: {e}")

        # Clean up trash
        print("   Emptying Trash folder...")
        try:
            deleted = empty_trash_folder(self.imap)
            print(f"   Deleted {deleted} emails from Trash")
        except Exception as e:
            print(f"   Error emptying trash: {e}")

        print(f"Cleanup complete: {total_archived} emails archived, {deleted} emails deleted")
        return {'archived': total_archived, 'deleted': deleted}

    def send_team_update(self, team_emails, subject, update_content):
        """Send update to entire team"""
        print(f"Sending team update to {len(team_emails)} team members...")
        print(f"   Subject: {subject}")

        success_count = 0

        for team_email in team_emails:
            print(f"   Sending to: {team_email}...")
            if send_email(
                sender_email=self.user_email,
                sender_password=self.password,
                recipient_email=team_email,
                subject=subject,
                body=update_content
            ):
                success_count += 1
                print(f"   Sent successfully to {team_email}")
            else:
                print(f"   Failed to send to {team_email}")

        print(f"Sent update to {success_count} out of {len(team_emails)} team members")
        return success_count

    def show_folder_structure(self):
        """Display detailed folder structure"""
        print("Email Folder Structure:")
        print("=" * 50)

        folders = list_all_folders(self.imap)

        for folder in sorted(folders):
            stats = get_folder_stats(self.imap, folder)
            print(f"[{folder}]")
            print(f"   Total: {stats['total']} | Unread: {stats['unread']}")
            print()

    def process_important_emails(self):
        """Process all important/flagged emails"""
        print("Processing important emails...")

        important_emails = find_flagged_emails(self.imap, 'INBOX')
        print(f"   Found {len(important_emails)} important emails in INBOX")

        processed_count = 0
        for email_id in important_emails:
            print(f"   Processing email {email_id.decode()}...")

            # Get email details
            emails = get_email_list(self.imap, 'INBOX', limit=50)
            email = next((e for e in emails if e['id'] == email_id.decode()), None)

            if email:
                print(f"      From: {email['from']}")
                print(f"      Subject: {email['subject']}")

                # Mark as read and move to Important folder
                if mark_email_as_read(self.imap, 'INBOX', email_id.decode()):
                    if move_email_to_folder(self.imap, email_id.decode(), 'INBOX', 'Important'):
                        processed_count += 1
                        print(f"      Moved to Important folder")
                    else:
                        print(f"      Failed to move to Important folder")

        print(f"Processed {processed_count} important emails")
        return processed_count

def main():
    parser = argparse.ArgumentParser(
        description='Email Management Automation Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Get email statistics
  python email_manager.py founder@mail.email founder123 --command stats

  # Generate email digest
  python email_manager.py founder@mail.email founder123 --command digest

  # Create project folder
  python email_manager.py founder@mail.email founder123 --command create-folder --folder "WebsiteRedesign"

  # Organize project emails
  python email_manager.py founder@mail.email founder123 --command organize --project "WebsiteRedesign" --keywords "website" "redesign" "UI"

  # Mark emails from sender as important
  python email_manager.py founder@mail.email founder123 --command mark-important --sender "client@example.com"

  # Send team update
  python email_manager.py founder@mail.email founder123 --command team-update --team-emails backend@mail.email frontend@mail.email --subject "Daily Update" --message "Team update here"
        """
    )

    parser.add_argument('user_email', help='Your email address (e.g., founder@mail.email)')
    parser.add_argument('password', help='Your email password')

    parser.add_argument('--command', choices=[
        'stats', 'digest', 'cleanup', 'mark-important', 'create-folder',
        'organize', 'team-update', 'folders', 'process-important', 'test'
    ], help='Command to execute', required=True)

    parser.add_argument('--folder', help='Folder name for create-folder command')
    parser.add_argument('--sender', help='Sender email for mark-important command')
    parser.add_argument('--project', help='Project name for organize command')
    parser.add_argument('--keywords', nargs='+', help='Keywords for organize command')
    parser.add_argument('--subject', help='Email subject for team-update command')
    parser.add_argument('--message', help='Email message for team-update command')
    parser.add_argument('--team-emails', nargs='+', help='Team emails for team-update command')
    parser.add_argument('--days', type=int, default=90, help='Days threshold for cleanup command (default: 90)')

    args = parser.parse_args()

    manager = EmailManager(args.user_email, args.password)

    if not manager.connect():
        print("Failed to connect to email server")
        return 1

    try:
        success = True

        if args.command == 'test':
            print("Testing connection...")
            folders = list_all_folders(manager.imap)
            print(f"Successfully connected! Found {len(folders)} folders")
            print(f"Folders: {', '.join(folders)}")

        elif args.command == 'stats':
            stats = get_email_statistics(manager.imap)
            print("Email Statistics:")
            print(json.dumps(stats, indent=2))

        elif args.command == 'folders':
            manager.show_folder_structure()

        elif args.command == 'digest':
            manager.email_digest()

        elif args.command == 'cleanup':
            manager.cleanup_old_emails(args.days)

        elif args.command == 'mark-important' and args.sender:
            manager.mark_emails_from_sender_as_important(args.sender)

        elif args.command == 'create-folder' and args.folder:
            manager.create_project_folder(args.folder)

        elif args.command == 'organize' and args.project and args.keywords:
            manager.organize_project_emails(args.keywords, args.project)

        elif args.command == 'process-important':
            manager.process_important_emails()

        elif args.command == 'team-update' and args.team_emails and args.subject and args.message:
            manager.send_team_update(args.team_emails, args.subject, args.message)

        else:
            print("Missing required arguments for command")
            print("Use --help for usage examples")
            success = False

    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        success = False
    except Exception as e:
        print(f"Error: {e}")
        success = False
    finally:
        manager.disconnect()

    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())
