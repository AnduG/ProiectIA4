from website.models import Statistics, User
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
        {"name": "Reaction Time", "value": make_stats_for(game_id=1)},
        {"name": "Sequence Memory", "value": make_stats_for(game_id=2)},
        {"name": "Word Generation", "value": make_stats_for(game_id=3)},
        {"name": "Matching Colors", "value": make_stats_for(game_id=4)},
        {"name": "placeholder1", "value": make_stats_for(game_id=5)},
        {"name": "placeholder2", "value": make_stats_for(game_id=6)}
    ]
    return all_stats

def upload_stats(game_id, game_results):
    new_stats = Statistics(owner_id=current_user.get_id(), type=game_id, results=game_results,)
    db.session.add(new_stats)
    db.session.commit()