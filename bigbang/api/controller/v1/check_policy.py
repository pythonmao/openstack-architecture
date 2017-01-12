import pecan
from bigbang.common import policy

def check_policy(book, action):
    context = pecan.request.context
    policy.enforce(context, action, book, action=action)