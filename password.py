import re


def password_check(password):

    score = 0

    if len(password) > 12:
        score += 2
    elif len(password) < 4:
        return

    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", password):
        score += 3
        if (
            re.search(r"[a-z]", password),
            re.search(r"[A-Z]", password),
            re.search(r"[0-9]", password),
            re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", password),
        ):
            score += 2

    return score
