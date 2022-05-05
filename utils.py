import json

DATA_FILE_PATH = "candidates.json"

def load_candidates_from_json(path):
    """Возвращает список всех кандидатов"""
    with open(path, "r", encoding="UTF-8") as file:
        return json.load(file)

def get_candidate(candidate_id):
    """Возвращает 1го кандидата по его id"""
    candidates = load_candidates_from_json(DATA_FILE_PATH)
    for candidate in candidates:
        if candidate['id'] == candidate_id:
            return candidate
    return None

def get_candidates_by_name(candidate_name):
    """Возвращает одного кандидата по его имени"""
    candidates = load_candidates_from_json(DATA_FILE_PATH)
    matches = []
    for candidate in candidates:
        if candidate_name.lower() in candidate["name"].lower():
            matches.append(candidate)
    return matches

def get_candidates_by_skill(skill_name):
    """Возвращает кандидатов по навыку"""
    candidates = load_candidates_from_json(DATA_FILE_PATH)
    matches = []
    for candidate in candidates:
        if skill_name.lower() in candidate["skills"].lower().split(", "):
            matches.append(candidate)
    return matches
