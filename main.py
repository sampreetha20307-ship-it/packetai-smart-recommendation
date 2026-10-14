# PacketAI Smart Recommendation and Assessment System
# Enhanced version for Naan Mudhalvan Project

class PacketAI:
    def __init__(self):
        # Comprehensive dataset of modules/packages with AI scoring metrics
        self.recommendations = [
            {"id": 1, "name": "AI Learning Module", "category": "Education", "score": 4.8, "difficulty": "Beginner"},
            {"id": 2, "name": "Cloud Deployment Tool", "category": "DevOps", "score": 4.5, "difficulty": "Intermediate"},
            {"id": 3, "name": "Smart Analytics Dashboard", "category": "Analytics", "score": 4.9, "difficulty": "Advanced"},
            {"id": 4, "name": "Automated Code Reviewer", "category": "Development", "score": 4.2, "difficulty": "Intermediate"},
            {"id": 5, "name": "Predictive Maintenance Kit", "category": "Analytics", "score": 4.7, "difficulty": "Advanced"}
        ]

    def get_top_recommendations(self):
        """Sorts and returns items based on their smart AI score."""
        return sorted(self.recommendations, key=lambda x: x["score"], reverse=True)

    def assess_user_preference(self, category):
        """Filters recommendations based on user choice/category."""
        matched = [item for item in self.recommendations if item["category"].lower() == category.lower()]
        return matched

    def generate_assessment_report(self):
        """Generates an evaluation report summary of all tracked items."""
        print("=== PacketAI Automated Assessment Report ===")
        total_items = len(self.recommendations)
        avg_score = sum(item["score"] for item in self.recommendations) / total_items
        print(f"Total Modules Managed: {total_items}")
        print(f"Overall System Quality Score: {avg_score:.2f} / 5.0\n")

if __name__ == "__main__":
    print("--- Initializing PacketAI Smart Recommendation & Assessment System ---\n")
    ai = PacketAI()
    
    # Run the assessment summary report
    ai.generate_assessment_report()
    
    print("Top Ranked Recommendations:")
    for item in ai.get_top_recommendations():
        print(f"* {item['name']} ({item['category']}) - Level: {item['difficulty']} [Score: {item['score']}]")
        
    print("\nFiltered Assessment (Category: Analytics):")
    results = ai.assess_user_preference("Analytics")
    for r in results:
        print(f"-> Match Found: {r['name']} (Score: {r['score']})")
