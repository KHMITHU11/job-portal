#!/usr/bin/env python
"""
Script to update contact information throughout the JobPortal application.
Replace the placeholder values with your actual contact information.
"""

import os
import re

# Your contact information - UPDATE THESE VALUES
CONTACT_INFO = {
    'email': 'your-email@example.com',
    'phone': '+1 (555) 123-4567',
    'location': 'Your Location',
    'business_hours': 'Monday - Friday: 9:00 AM - 6:00 PM\nSaturday: 10:00 AM - 2:00 PM',
    'linkedin': 'https://linkedin.com/in/your-profile',
    'twitter': 'https://twitter.com/your-handle',
    'facebook': 'https://facebook.com/your-page',
    'instagram': 'https://instagram.com/your-handle',
    'github': 'https://github.com/your-username'
}

def update_file_content(file_path, replacements):
    """Update file content with new contact information"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Apply all replacements
        for old_text, new_text in replacements.items():
            content = content.replace(old_text, new_text)
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        
        print(f"✅ Updated: {file_path}")
        return True
    except Exception as e:
        print(f"❌ Error updating {file_path}: {e}")
        return False

def main():
    print("🔄 Updating contact information throughout the application...")
    print(f"📧 Email: {CONTACT_INFO['email']}")
    print(f"📞 Phone: {CONTACT_INFO['phone']}")
    print(f"📍 Location: {CONTACT_INFO['location']}")
    print()
    
    # Files to update with their replacements
    files_to_update = {
        'templates/base.html': {
            'your-email@example.com': CONTACT_INFO['email'],
            '+1 (555) 123-4567': CONTACT_INFO['phone'],
            'Your Location': CONTACT_INFO['location']
        },
        'templates/jobs/contact.html': {
            'your-email@example.com': CONTACT_INFO['email'],
            '+1 (555) 123-4567': CONTACT_INFO['phone'],
            'Your Location': CONTACT_INFO['location'],
            'Monday - Friday: 9:00 AM - 6:00 PM<br>\n                        Saturday: 10:00 AM - 2:00 PM': CONTACT_INFO['business_hours'].replace('\n', '<br>\n                        '),
            'href="#"': f'href="{CONTACT_INFO["linkedin"]}"',
            'href="#"': f'href="{CONTACT_INFO["twitter"]}"',
            'href="#"': f'href="{CONTACT_INFO["facebook"]}"',
            'href="#"': f'href="{CONTACT_INFO["instagram"]}"'
        },
        'README.md': {
            'your-email@example.com': CONTACT_INFO['email'],
            '+1 (555) 123-4567': CONTACT_INFO['phone'],
            'Your Location': CONTACT_INFO['location'],
            '[Your GitHub Profile]': CONTACT_INFO['github'],
            '[Your LinkedIn Profile]': CONTACT_INFO['linkedin']
        }
    }
    
    success_count = 0
    total_files = len(files_to_update)
    
    for file_path, replacements in files_to_update.items():
        if os.path.exists(file_path):
            if update_file_content(file_path, replacements):
                success_count += 1
        else:
            print(f"⚠️  File not found: {file_path}")
    
    print(f"\n🎉 Contact information update complete!")
    print(f"✅ Successfully updated {success_count}/{total_files} files")
    
    if success_count == total_files:
        print("\n📋 Next steps:")
        print("1. Review the updated files to ensure accuracy")
        print("2. Test the contact form at /contact/")
        print("3. Update social media links if needed")
        print("4. Consider adding your actual business hours")
        print("5. Test the application to ensure everything works")
    else:
        print("\n⚠️  Some files could not be updated. Please check manually.")

if __name__ == '__main__':
    print("=" * 60)
    print("🔧 JobPortal Contact Information Updater")
    print("=" * 60)
    print()
    print("This script will update your contact information throughout")
    print("the JobPortal application. Please update the CONTACT_INFO")
    print("dictionary at the top of this file with your actual details.")
    print()
    
    # Ask for confirmation
    response = input("Do you want to proceed with the current contact information? (y/n): ")
    if response.lower() in ['y', 'yes']:
        main()
    else:
        print("Please update the CONTACT_INFO dictionary and run again.") 