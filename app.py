import streamlit as st

def bmi(weight_kg, height_cm):
    if (weight_kg <= 0) or (height_cm <= 0):
        raise ValueError("Weight and height must be greater than zero")

    height_m = height_cm / 100
    bmi_value = weight_kg / (height_m ** 2)

    if bmi_value < 18.5:
        category = "Underweight"
    elif bmi_value < 25:
        category = "Normal weight"
    elif bmi_value < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return round(bmi_value, 1), category


def score_stats(scores):
    if not scores:
        return {"max": 0, "min": 0, "avg": 0.0, "count": 0}

    return {
        "max": max(scores),
        "min": min(scores),
        "avg": sum(scores) / len(scores),
        "count": len(scores),
    }


def parse_scores(text: str):
    return [int(s.strip()) for s in text.split(",") if s.strip().isdigit()]

def summary(text):
    scores = parse_scores(text)
    stats = score_stats(scores)

    grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for s in scores:
        if s >= 90:
            grade_counts["A"] += 1
        elif s >= 80:
            grade_counts["B"] += 1
        elif s >= 70:
            grade_counts["C"] += 1
        elif s >= 60:
            grade_counts["D"] += 1
        else:
            grade_counts["F"] += 1

    stats["grades"] = grade_counts
    stats["scores"] = scores
    return stats

st.sidebar.title("Navigation Sidebar")
page = st.sidebar.selectbox(
    "Select a page",
    ("BMI Calculator", "Score Stats", "Marks Summary")
)

if page == "BMI Calculator":
    st.header("BMI Calculator")

    weight_kg = st.number_input("Enter weight (kg): ", min_value=0.0)
    height_cm = st.number_input("Enter height (cm): ", min_value=0.0)
    press_button = st.button("Compute BMI")

    if press_button:
        value, category = bmi(weight_kg, height_cm)
        st.success(f"BMI: {value}, Category: {category}")


elif page == "Score Stats":
    st.header("Score Stats")

    scores_str = st.text_input("Enter scores separated by comma")
    if scores_str:
        scores = parse_scores(scores_str)
        st.write(score_stats(scores))

elif page == "Marks Summary":
    st.header("Marks Summary")

    scores_text = st.text_area("Enter scores separated by commas")

    if scores_text:
        results = summary(scores_text)

        st.subheader("Statistics")
        st.write({
            "Max": results["max"],
            "Min": results["min"],
            "Average": results["avg"],
            "Count": results["count"]
        })

        st.subheader("Grade Counts")
        st.table(results["grades"])
        st.subheader("Scores Chart")
        st.bar_chart(results["scores"])
