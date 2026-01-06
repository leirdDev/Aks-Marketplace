from dataclasses import dataclass
from allauth.headless.adapter import DefaultHeadlessAdapter

@dataclass
class UserPayload:
    id: int
    email: str
    username: str
    first_name: str
    last_name: str
    has_usable_password: bool
    profile_url: str


class CustomHeadlessAdapter(DefaultHeadlessAdapter):
    def get_user_dataclass(self):
        return UserPayload

    def user_as_dataclass(self, user):
        return UserPayload(
            id=user.id,
            email=user.email,
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            has_usable_password=user.has_usable_password(),
            profile_url=user.profile_url or "",
        )
