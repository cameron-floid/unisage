import bcrypt


class SecurityUtils:
    @staticmethod
    def verify_password(password: str, password_hash: str) -> bool:
        """
        Verify a password against its hashed version.

        Args:
            password (str): The plain-text password to verify.
            password_hash (str): The hashed password stored in the database.

        Returns:
            bool: True if the password matches the hash, False otherwise.
        """
        try:
            return bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8'))
        except Exception as e:
            # Handle exceptions, such as invalid hash or password
            print(f"Error verifying password: {str(e)}")
            return False

    @staticmethod
    def hash_password(password: str) -> str:
        """
        Hash a password using bcrypt.

        Args:
            password (str): The plain-text password to hash.

        Returns:
            str: The hashed password as a string.
        """
        try:
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
            return hashed_password.decode('utf-8')

        except Exception as e:
            # Handle exceptions, if any
            print(f"Error hashing password: {str(e)}")
            return ''
