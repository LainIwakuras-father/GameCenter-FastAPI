import os
import sys
from pathlib import Path
from app.models.user import User


os.environ["ADMIN_USER_MODEL"] = "app.models.User"
os.environ["ADMIN_USER_MODEL_USERNAME_FIELD"] = "username"
os.environ["ADMIN_SECRET_KEY"] = "om_l%3lt44w1cu)k@!u%pt_gg6_)*om1*k)&o##3_p!u8lvrh="

sys.path.append(str(Path(__file__).resolve().parent))