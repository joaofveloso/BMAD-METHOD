# Email Automation Guide

This guide explains how each container can send automated emails using the built-in email automation system.

## Quick Start

Each container comes with pre-configured email capabilities. Inside any container:

```bash
# Check email configuration
setup-email

# Send a test email
email send qa@mail.email "Hello from $(hostname)" "This is a test email"

# Send status report
email status admin@mail.email

# Send alert
email alert "Test Alert" "This is a test alert message"
```

## Available Email Commands

### 1. Basic Email Sending

```bash
# Send simple email
email send <recipient> <subject> <message>

# Example:
email send devops@mail.email "Deployment Complete" "Backend deployment finished successfully"
```

### 2. Status Reports

```bash
# Send comprehensive status report
email status [recipient]

# Example:
email status admin@mail.email

# Includes: uptime, memory, disk usage, running processes, network status
```

### 3. Log File Sending

```bash
# Send log file content
email logs [recipient] [logfile] [lines]

# Examples:
email logs admin@mail.email /var/log/syslog 100
email logs devops@mail.email /var/log/nginx/error.log 50
```

### 4. Alert Emails

```bash
# Send alert email
email alert <alert_type> <message> [recipient]

# Examples:
email alert "High CPU Usage" "CPU usage is above 90%" admin@mail.email
email alert "Disk Space" "Root partition 95% full" devops@mail.email
```

### 5. Scheduled Emails

```bash
# Setup automated email scheduling
email schedule <type> <recipient>

# Types: hourly, daily, weekly
# Examples:
email schedule daily admin@mail.email    # Daily status at 8 AM
email schedule hourly qa@mail.email      # Hourly status reports
email schedule weekly devops@mail.email  # Weekly reports Monday 8 AM
```

### 6. Configuration Check

```bash
# Show current email configuration
email config

# Shows: email account, SMTP settings, container name
```

## Email Credentials by Container

Each container has its own email account:

| Container    | Email Address           | Password        |
| ------------ | ----------------------- | --------------- |
| founder      | founder@mail.email      | founder123      |
| orchestrator | orchestrator@mail.email | orchestrator123 |
| backend      | backend@mail.email      | backend123      |
| frontend     | frontend@mail.email     | frontend123     |
| mobile       | mobile@mail.email       | mobile123       |
| qa           | qa@mail.email           | qa123           |
| devops       | devops@mail.email       | devops123       |
| researcher   | researcher@mail.email   | researcher123   |

## Use Cases and Examples

### 1. Deployment Notifications

```bash
# From backend container after deployment:
email send qa@mail.email "Backend Deployed" "New backend version deployed to production. Please run tests."
email send devops@mail.email "Backend Deployed" "Backend deployment completed successfully. Version: v1.2.3"
```

### 2. Health Monitoring

```bash
# Automated health check script:
#!/bin/bash
if ! curl -f http://localhost:3000/health > /dev/null 2>&1; then
    email alert "Service Down" "Backend service is not responding" admin@mail.email
fi
```

### 3. Log Monitoring

```bash
# Send error logs when issues detected:
if grep -i "error" /var/log/app.log | tail -10; then
    email logs devops@mail.email /var/log/app.log 20
fi
```

### 4. Resource Monitoring

```bash
# Disk space monitoring:
DISK_USAGE=$(df / | tail -1 | awk '{print $5}' | sed 's/%//')
if [ $DISK_USAGE -gt 80 ]; then
    email alert "Disk Usage High" "Disk usage is ${DISK_USAGE}%" admin@mail.email
fi
```

### 5. Automated Reports

```bash
# Daily system report:
email status admin@mail.email

# Weekly project summary:
email send researcher@mail.email "Weekly Summary" "Research progress update for this week..."
```

## Integration with Scripts

### Example 1: Backup Notification

```bash
#!/bin/bash
# backup-script.sh
echo "Starting backup..."
if tar -czf /backup/$(date +%Y%m%d).tar.gz /important/data; then
    email send admin@mail.email "Backup Complete" "Backup successful: $(date +%Y%m%d).tar.gz"
else
    email alert "Backup Failed" "Backup process failed on $(date)"
fi
```

### Example 2: Test Results

```bash
#!/bin/bash
# run-tests.sh
echo "Running tests..."
if npm test; then
    email send devops@mail.email "Tests Passed" "All tests passed successfully"
else
    email alert "Tests Failed" "Test suite failed - check logs"
    email logs devops@mail.email /var/log/test.log 50
fi
```

### Example 3: Service Monitor

```bash
#!/bin/bash
# monitor-services.sh
services=("nginx" "redis" "postgresql")
for service in "${services[@]}"; do
    if ! systemctl is-active --quiet $service; then
        email alert "Service Down" "$service is not running" admin@mail.email
    fi
done
```

## Environment Variables

Each container has these email-related environment variables:

```bash
EMAIL_ACCOUNT=<container_name>@mail.email
EMAIL_PASSWORD=<container_password>
```

## SMTP Configuration

All containers use these SMTP settings:

- **Server**: mail.email
- **Port**: 587 (STARTTLS)
- **Authentication**: Required
- **Username**: Full email address
- **Password**: Container-specific password

## Advanced Usage

### Email Templates

```bash
# Create reusable email templates
cat > /usr/local/bin/email-template.sh << 'EOF'
#!/bin/bash
TEMPLATE_NAME=$1
RECIPIENT=$2

case $TEMPLATE_NAME in
    "deployment")
        email send "$RECIPIENT" "Deployment Notice" "Deployment completed at $(date)"
        ;;
    "error")
        email send "$RECIPIENT" "Error Occurred" "An error was detected in the system"
        ;;
esac
EOF
chmod +x /usr/local/bin/email-template.sh
```

### Email Pipelines

```bash
# Chain email notifications
echo "Process completed" | email send qa@mail.email "Process Complete" -
email status admin@mail.email
```

### Conditional Emailing

```bash
# Send email only on certain conditions
if [ $SUCCESS = true ]; then
    email send stakeholder@mail.email "Success" "Operation completed successfully"
else
    email alert "Failure" "Operation failed - investigation needed"
fi
```

## Python Email API

Use the included Python scripts for programmatic email access:

```python
from email_processor import *

# Connect to email server
imap = connect_email_server('founder@mail.email', 'founder123')

# Search for project emails
emails = search_by_subject(imap, 'INBOX', 'project')

# Move emails to folders
move_email_to_folder(imap, '123', 'INBOX', 'Projects')

# Mark as important
mark_email_as_important(imap, 'INBOX', '123')

# Send HTML email
send_html_email('founder@mail.email', 'founder123', 'team@mail.email', 'Update', html_content)

# Disconnect
imap.logout()
```

### CLI Management Tool

```bash
# Get email statistics
python email_manager.py founder@mail.email founder123 --command stats

# Generate daily digest
python email_manager.py founder@mail.email founder123 --command digest

# Clean up old emails
python email_manager.py founder@mail.email founder123 --command cleanup

# Send team update
python email_manager.py founder@mail.email founder123 --command team-update \
    --team-emails backend@mail.email frontend@mail.email \
    --subject "Daily Update" --message "Team update here"
```

## Troubleshooting

### Common Issues

1. **Email not sending**: Check network connectivity to mail.email
2. **Authentication failed**: Verify email account and password
3. **SMTP connection error**: Ensure mail server is running

### Debug Commands

```bash
# Check email configuration
email config

# Test network connectivity
ping mail.email

# Check SMTP connection
telnet mail.email 587

# Check environment variables
echo $EMAIL_ACCOUNT
echo $EMAIL_PASSWORD
```

## Security Notes

- Email passwords are simple for development - change in production
- Consider using app-specific passwords for production
- Email content is sent unencrypted within the private network
- Use HTTPS for webmail access

## Best Practices

1. **Use meaningful subject lines** for easy filtering
2. **Include container name** in emails for identification
3. **Schedule emails** appropriately to avoid spam
4. **Monitor email delivery** for important notifications
5. **Use alert emails** sparingly for critical issues only
