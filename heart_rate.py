"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum.
"""

print("Please enter your age.")
age_input = int(input(">> "))
maximum_heart_rate = 220 - age_input
bottom_range = maximum_heart_rate * .65
top_range = maximum_heart_rate * .85

print(f"When you exercise to strengthen your heart, you should keep your heart rate between {bottom_range:.0f} and {top_range:.0f} beats per minute.")