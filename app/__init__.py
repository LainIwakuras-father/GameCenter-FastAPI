import os
import sys
from pathlib import Path

os.environ["ADMIN_USER_MODEL"] = "User"
os.environ["ADMIN_USER_MODEL_USERNAME_FIELD"] = "username"
os.environ["ADMIN_SECRET_KEY"] = "4cbdecd4b9e939f562f79d172e188b29"

sys.path.append(str(Path(__file__).resolve().parent))