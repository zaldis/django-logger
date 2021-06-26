from changelog.models.changelog import create_log_model


logged_models = []


def track_model_changes(model):
    logged_models.append(model)
    create_log_model(model)

    return model
