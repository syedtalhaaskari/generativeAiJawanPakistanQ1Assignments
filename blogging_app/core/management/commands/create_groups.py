from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    help = 'Create default user groups'

    def handle(self, *args, **kwargs):
        # Define groups and associated permissions
        all_permissions = Permission.objects.values_list("codename", flat=True).all()

        # all_permissions.
        groups_permissions = {
            'Superuser': all_permissions,
            'Moderator': ['add_logentry', 'view_logentry', 'add_permission', 'change_permission', 'view_permission', 'view_group', 'view_user', 'add_contenttype', 'change_contenttype', 'view_contenttype', 'add_session', 'change_session', 'delete_session', 'view_session', 'add_category', 'change_category', 'delete_category', 'view_category', 'add_post', 'change_post', 'delete_post', 'view_post', 'add_comment', 'change_comment', 'delete_comment', 'view_comment', 'add_like', 'change_like', 'delete_like', 'view_like'],
            'Author': ['view_logentry', 'view_user', 'add_contenttype', 'change_contenttype', 'view_contenttype', 'add_session', 'change_session', 'delete_session', 'view_session', 'add_post', 'change_post', 'delete_post', 'view_post', 'add_comment', 'change_comment', 'delete_comment', 'view_comment', 'add_like', 'change_like', 'delete_like', 'view_like'],
            'Reader': ['view_user', 'add_contenttype', 'change_contenttype', 'view_contenttype', 'add_session', 'change_session', 'delete_session', 'view_session', 'view_post', 'add_comment', 'change_comment', 'delete_comment', 'view_comment', 'add_like', 'change_like', 'delete_like', 'view_like'],
        }

        # Create groups and assign permissions
        for group_name, perm_codes in groups_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            if created:
                self.stdout.write(f'Group "{group_name}" created.')
            else:
                self.stdout.write(f'Group "{group_name}" already exists.')

            # Add permissions to the group
            for perm_code in perm_codes:
                try:
                    permission = Permission.objects.get(codename=perm_code)
                    group.permissions.add(permission)
                except Permission.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f'Permission "{perm_code}" not found.'))

        self.stdout.write(self.style.SUCCESS('Groups and permissions successfully created.'))
