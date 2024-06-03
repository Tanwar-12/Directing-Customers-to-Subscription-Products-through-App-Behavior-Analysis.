def analyze_behavior(user_data):
    # Extract features from user_data
    num_sessions = float(user_data.get('num_sessions', 0))
    avg_session_duration = float(user_data.get('avg_session_duration', 0))
    num_clicks = float(user_data.get('num_clicks', 0))
    pages_visited = float(user_data.get('pages_visited', 0))
    time_on_page = float(user_data.get('time_on_page', 0))
    previous_subscriptions = float(user_data.get('previous_subscriptions', 0))

    # This is where you'd typically load your model and make a prediction
    # For example:
    # model = load_model('path/to/your/model')
    # prediction = model.predict([[
    #     num_sessions, avg_session_duration, num_clicks,
    #     pages_visited, time_on_page, previous_subscriptions
    # ]])

    # Dummy prediction for illustration purposes
    prediction = "Basic Subscription" if num_sessions > 5 else "Premium Subscription"

    return prediction
