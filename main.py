# PacketAI Smart Recommendation and Assessment System

class PacketAI:
    def __init__(self):
        # Sample dataset of items/packages with features and scores
        self.recommendations = [
            {"id": 1, "name": "AI Learning Module", "category": "Education", "score": 4.8},
            {"id": 2, "name": "Cloud Deployment Tool", "category": "DevOps", "score": 4.5},
            {"id": 3, "name": "Smart Analytics Dashboard", "category": "Analytics", "score": 4.9},
            {"id": 4, "name": "Automated Code Reviewer", "category": "Development", "score": 4.2}
        ]

    def get_top_recommendations(self):
        """Sorts and returns items based on their smart score."""
        sorted_items = sorted(self.recommendations, key=lambda x: x["score"], reverse=True)
        return sorted_items

    def assess_user_preference(self, category):
        """Filters recommendations based on user choice."""
        matched = [item for item in self.recommendations if item["category"].lower() == category.lower()]
        return matched

if __name__ == "__main__":
    print("--- Initializing PacketAI Smart Recommendation & Assessment ---")
    ai = PacketAI()
    
    print("\nTop Recommendations:")
    for item in ai.get_top_recommendations():
        print(f"- {item['name']} ({item['category']}) [Score: {item['score']}]")
        
    print("\nAssessment Filter Test (Category: Analytics):")
    results = ai.assess_user_preference("Analytics")
    for r in results:
        print(f"Found match: {r['name']}")
