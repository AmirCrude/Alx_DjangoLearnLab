# Permissions and Groups Setup

## Custom Permissions

The Book model includes custom permissions:
- can_view
- can_create
- can_edit
- can_delete

These permissions are defined inside the Meta class of the Book model.

## Groups

Three groups were created:
- Viewers → can_view
- Editors → can_view, can_create, can_edit
- Admins → all permissions

## View Protection

Views are protected using Django's @permission_required decorator.

Example:
@permission_required('bookshelf.can_edit', raise_exception=True)

If a user does not have the required permission, a 403 Forbidden error is raised.

## Testing

Users were created and assigned to different groups to verify:
- Permission inheritance works correctly.
- Access is restricted based on group membership.
