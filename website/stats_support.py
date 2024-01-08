from website.models import Statistics, Activities
from flask_login import current_user
from . import db

def get_all_data_for(game_id):
    return Statistics.query.filter_by(owner_id=current_user.get_id(), type=game_id).all()

def get_attempt_count(game_id):
    stats = Statistics.query.filter_by(owner_id=current_user.get_id(), type=game_id).all()
    results = [stat.results for stat in stats]
    return len(results)

def get_best_attempt_for(game_id):
    stat = Statistics.query.filter_by(owner_id=current_user.get_id(), type=game_id).\
        order_by(Statistics.results.desc()).first()
    if stat:
        return stat.results
    else: 
        return 0

def get_latest_attempt_for(game_id):
    stat = Statistics.query.filter_by(owner_id=current_user.get_id(), type=game_id).\
        order_by(Statistics.created_at.desc()).first()
    if stat:
        return stat.results
    else: 
        return 0

def get_average_attempt_for(game_id):
    stats = Statistics.query.filter_by(owner_id=current_user.get_id(), type=game_id).all()
    results = [stat.results for stat in stats]
    if len(results) == 0:
        return 0
    else:
        return sum(results) / len(results)

def get_global_average_for(game_id):
    stats = Statistics.query.filter_by(type=game_id).all()
    results = [stat.results for stat in stats]
    if len(results) == 0:
        return 0
    else:
        return sum(results) / len(results)

def make_stats_for(game_id):
    stats = [
        {"name": "Attempt Count", "value": get_attempt_count(game_id=game_id)},
        {"name": "Best Attempt", "value": get_best_attempt_for(game_id=game_id)},
        {"name": "Latest Attempt", "value": get_latest_attempt_for(game_id=game_id)},
        {"name": "Average Attempt", "value": get_average_attempt_for(game_id=game_id)},
        {"name": "Global Average", "value": get_global_average_for(game_id=game_id)}
    ]
    return stats

def make_stats():
    all_stats = [
        {"name": "Reaction Time", "value": make_stats_for(game_id=Activities.reaction_time.name)},
        {"name": "Sequence Memory", "value": make_stats_for(game_id=Activities.sequence_memory.name)},
        {"name": "Word Generation", "value": make_stats_for(game_id=Activities.word_generation.name)},
        {"name": "Matching Colors", "value": make_stats_for(game_id=Activities.matching_colors.name)},
        {"name": "Pattern Memory", "value": make_stats_for(game_id=Activities.pattern_memory.name)},
        {"name": "Quick Calculus", "value": make_stats_for(game_id=Activities.quick_calculus.name)},
        {"name": "Aim Training", "value": make_stats_for(game_id=Activities.aim_training.name)},
        {"name": "Writing Test", "value": make_stats_for(game_id=Activities.fast_typing.name)}
    ]
    return all_stats

def upload_stats(game_id, game_results):
    new_stats = Statistics(owner_id=current_user.get_id(), type=game_id, results=game_results,)
    db.session.add(new_stats)
    db.session.commit()