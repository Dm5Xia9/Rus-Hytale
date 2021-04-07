def get_or_none(model, *args, **kwargs):
    try:
        return model.objects.get(*args, **kwargs)
    except model.DoesNotExist:
        return None
from accounts.models import User
def messages_users_get(messages_count):
    if (len(User.objects.order_by('-messages_count')) < messages_count):
        Users_messages_count = User.objects.order_by('-messages_count')[:len(User.objects.order_by('-messages_count'))]
    else:
        Users_messages_count = User.objects.order_by('-messages_count')[:messages_count]
    return Users_messages_count
def points_users_get(Points):
    if (len(User.objects.order_by('-Points')) < Points):
        Users_Points = User.objects.order_by('-Points')[:len(User.objects.order_by('-Points'))]
    else:
        Users_Points = User.objects.order_by('-Points')[:Points]
    return Users_Points
def IntorNone(object, default):
    try:
        return int(object)
    except ValueError:
        return default
