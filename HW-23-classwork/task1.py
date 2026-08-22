import unittest


# მოცემული ფუნქციები
def get_allowed_users():
    return ["john", "jane", "bob", "alice"]


def register_user(username):
    return username.lower()


# ტესტები unittest-ის გამოყენებით
class TestUserRegistration(unittest.TestCase):

    # ტესტი 1: რეგისტრირებული "John" უნდა იყოს ნებადართულ მომხმარებლებში
    def test_registered_user_in_allowed(self):
        allowed_users = get_allowed_users()
        user = register_user("John")
        self.assertIn(user, allowed_users)

    # ტესტი 2: assertIn და assertNotIn-ის შემოწმება
    def test_user_existence(self):
        allowed_users = get_allowed_users()
        self.assertIn("john", allowed_users)
        self.assertIn("alice", allowed_users)
        self.assertNotIn("dato", allowed_users)


if __name__ == "__main__":
    unittest.main()
