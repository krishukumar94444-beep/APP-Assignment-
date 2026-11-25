
import logging

# Configure logging system
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("application.log", mode="w"),
        logging.StreamHandler()
    ],
    force=True
)

# Create logger
logger = logging.getLogger()

# Display messages of different severity levels
logger.debug("This is a DEBUG message.")
logger.info("Program started successfully.")
logger.warning("This is a WARNING message.")
logger.error("An ERROR occurred while processing data.")
logger.critical("CRITICAL: System failure detected!")

print("\nLogging messages recorded successfully.")
print("Check the application.log file for saved logs.")

Comment :-
2026-11-25 20:00:00,123 - DEBUG - This is a DEBUG message.
2026-11-25 20:00:00,124 - INFO - Program started successfully.
2026-11-25 20:00:00,125 - WARNING - This is a WARNING message.
2026-11-25 20:00:00,126 - ERROR - An ERROR occurred while processing data.
2026-11-25 20:00:00,127 - CRITICAL - CRITICAL: System failure detected!

Logging messages recorded successfully.
Check the application.log file for saved logs.
