from loguru import logger
import sys
from pathlib import Path

# # 📂 Папка для логов
# LOG_DIR = Path(__file__).resolve().parent.parent.parent / "logs"
# LOG_DIR.mkdir(parents=True, exist_ok=True)

# 🧹 Очищаем все старые хендлеры (иначе будут дубли)
logger.remove()

# 1️⃣ Логи в консоль (удобно для Docker/k8s)
logger.add(
    sys.stdout,
    colorize=True,
    #для дева
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
           "<level>{level: <8}</level> : "
           "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
           "<level>{message}</level>",
    level="INFO",  # на проде можно ставить WARNING
)

# Экспортируем готовый logger
app_logger = logger