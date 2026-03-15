import streamlit as st

# Professional Header
st.title("🏠 DormHarmony")
st.subheader("AI-Based Roommate Compatibility Matcher")
st.write("Finding your perfect roommate using Constraint Satisfaction & Heuristics.")

# --- SIDEBAR: User Input ---
st.sidebar.header("Your Living Habits")

# Our 10 Attributes
sleep = st.sidebar.select_slider("Sleep Schedule", options=[1, 2, 3, 4, 5], help="1: Early Bird, 5: Night Owl")
clean = st.sidebar.select_slider("Cleanliness", options=[1, 2, 3, 4, 5], help="1: Messy, 5: Neat Freak")
noise = st.sidebar.select_slider("Noise Tolerance", options=[1, 2, 3, 4, 5])
social = st.sidebar.select_slider("Social Battery", options=[1, 2, 3, 4, 5])
ac = st.sidebar.select_slider("AC Preference", options=[1, 2, 3, 4, 5], help="1: Ice Cold, 5: Fan Only")
share = st.sidebar.select_slider("Shared Supplies", options=[1, 2, 3, 4, 5])
lights = st.sidebar.select_slider("Lights Out Time", options=[1, 2, 3, 4, 5])
smoke = st.sidebar.radio("Do you smoke?", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")

user_habits = [sleep, clean, noise, social, ac, share, lights, smoke]

# --- THE AI BRAIN (Logic from previous step) ---
def get_match_score(user, candidate):
    if user[-1] != candidate[-1]: # Hard Constraint
        return 0
    weights = [2, 1, 2, 1, 2, 1, 1, 0] 
    diff = sum(abs(u - c) * w for u, c, w in zip(user, candidate, weights))
    max_diff = sum(4 * w for w in weights)
    return round((1 - (diff / max_diff)) * 100, 2)

# --- MOCK DATABASE ---
candidates = [
    {"name": "Aditya (ECE)", "habits": [1, 5, 1, 1, 1, 2, 1, 0]}, # The Perfect Quiet Roomie
    {"name": "Riya (CSE)", "habits": [5, 2, 4, 5, 5, 4, 5, 0]},   # The Night Owl
    {"name": "Karthik (Mech)", "habits": [3, 3, 3, 3, 3, 3, 3, 1]}, # The Smoker (Hard Constraint Test)
    {"name": "Sana (BioTech)", "habits": [2, 4, 2, 2, 5, 3, 2, 0]}, # Cold AC Lover
    {"name": "Vijay (ECE)", "habits": [4, 1, 5, 5, 3, 5, 4, 0]},   # Messy & Loud
]
# --- EXECUTION ---
if st.button("Find My Match"):
    with st.spinner('AI is analyzing state-space constraints...'):
        import time
        time.sleep(1) # This simulates the AI "thinking" time

    st.write("### AI Analysis Results:")
    
    # Sort candidates by score so the best match is at the top
    results = []
    for person in candidates:
        score = get_match_score(user_habits, person['habits'])
        results.append({"name": person['name'], "score": score})
    
    # Advanced Sorting: This is the 'Selection' part of AI
    results = sorted(results, key=lambda x: x['score'], reverse=True)

    for res in results:
        score = res['score']
        name = res['name']
        
        if score > 0:
            # Displays a professional progress bar for each match
            st.write(f"**{name}**")
            st.progress(int(score)) 
            st.caption(f"Compatibility Score: {score}%")
            
            if score > 85:
                st.success("🌟 Highly Compatible (Optimal State Found)")
        else:
            st.error(f"❌ {name}: 0% Match (Hard Constraint: Smoking Violation)")