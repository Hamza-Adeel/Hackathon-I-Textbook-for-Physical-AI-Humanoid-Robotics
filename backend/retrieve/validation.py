import logging
import sys
sys.path.append('.')
from retrieval import semantic_search

logging.basicConfig(filename='retrieve/validation.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s',
                    filemode='w', encoding='utf-8')

TEST_QUERIES = [
    # General
    "What is a URDF file?",
    "How do I launch a ROS 2 node?",
    "What is the difference between a topic and a service?",
    # ROS 2
    "Explain ROS 2 nodes in Python.",
    "What is rclpy?",
    "How to create a ROS 2 package?",
    # Gazebo
    "What is Gazebo?",
    "How do I use a digital twin for robot simulation?",
    "How to simulate sensors in Gazebo?",
    # NVIDIA Isaac
    "What is NVIDIA Isaac Sim?",
    "How can I use synthetic data for training a robot?",
    "What is Isaac ROS vSLAM?",
    # VLA
    "What is a Vision-Language-Action model?",
    "How do I use whisper for voice commands?",
    "What is a cognitive planner?",
]

def run_validation():
    """Runs the validation by executing the test queries."""
    for query in TEST_QUERIES:
        logging.info(f"--- Query: {query} ---")
        results = semantic_search(query)
        if results:
            for result in results:
                log_message = (
                    f"  Score: {result.score:.4f}, "
                    f"ID: {result.id}, "
                    f"Source: {result.payload.get('source_url', 'N/A')}, "
                    f"Text: {result.payload.get('text', 'N/A')[:200]}..."
                )
                logging.info(log_message)
        else:
            logging.info("  No results found.")

if __name__ == '__main__':
    run_validation()