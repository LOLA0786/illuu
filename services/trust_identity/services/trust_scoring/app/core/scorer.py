RISK_KEYWORDS = ["urgent", "wire", "transfer", "confidential", "immediately"]

behavior_history = {}

def calculate_score(identity_verified: bool, device_match: bool, message: str, email: str):
    score = 100

    if not identity_verified:
        score -= 40

    if not device_match:
        score -= 25

    keyword_hits = sum(1 for word in RISK_KEYWORDS if word in message.lower())
    score -= keyword_hits * 5

    # Behavioral anomaly tracking
    if email not in behavior_history:
        behavior_history[email] = 0

    if keyword_hits > 1:
        behavior_history[email] += 1

    if behavior_history[email] > 3:
        score -= 15  # anomaly penalty

    if score < 0:
        score = 0

    return score
