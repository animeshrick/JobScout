from django.urls import path

from users.views.all_users import AllUsersView
from users.views.create_user import CreateUsersView
from users.views.otp_view import SendOTPView
from users.views.password_reset import PasswordResetView
from users.views.refresh_token import RefreshTokenView
from users.views.remove_user import RemoveUserView
from users.views.search_user import SearchUsersView
from users.views.sign_in import SignInView
from users.views.update_password import UpdatePasswordView
from users.views.update_profile import UpdateProfileView
from users.views.user_details import UserDetailView
from users.views.validate_otp_view import ValidateOTPView

urlpatterns = [
    path("create-users", CreateUsersView.as_view(), name="Create-Users"),
    path("sign-in", SignInView.as_view(), name="user-sign-in"),
    path("update-profile", UpdateProfileView.as_view(), name="Update-User-profile"),
    path("user-details", UserDetailView.as_view(), name="user-details"),
    path("all-users", AllUsersView.as_view(), name="All-Users"),
    path("remove-user", RemoveUserView.as_view(), name="Remove-User"),
    path("send-otp", SendOTPView.as_view(), name="send-otp"),
    path("verify-otp", ValidateOTPView.as_view(), name="verify-otp"),
    path(
        "reset-password",
        PasswordResetView.as_view(),
        name="send-reset-password-email",
    ),
    path("update-password", UpdatePasswordView.as_view(), name="Change-User-Password"),
    path("refresh-token", RefreshTokenView.as_view(), name="refresh-token"),
    path("search-users", SearchUsersView.as_view(), name="Search-Users"),
    # path("clear-caches", ClearServerCaches.as_view(), name="clear-caches"),
]
