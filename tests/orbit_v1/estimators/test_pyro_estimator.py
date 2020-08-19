from orbit_v1.estimators.pyro_estimator import PyroEstimatorVI, PyroEstimatorMAP


def test_pyro_estimator_vi(stan_estimator_lgt_model_input):
    stan_model_name, model_param_names, data_input = stan_estimator_lgt_model_input

    # create estimator
    vi_estimator = PyroEstimatorVI()

    # extract posterior samples
    stan_extract = vi_estimator.fit(
        stan_model_name=stan_model_name,
        model_param_names=model_param_names,
        data_input=data_input
    )

    expected_extract_keys = model_param_names[:]

    assert set(expected_extract_keys) == set(stan_extract.keys())


def test_pyro_estimator_map(stan_estimator_lgt_model_input):
    stan_model_name, model_param_names, data_input = stan_estimator_lgt_model_input

    # create estimator
    vi_estimator = PyroEstimatorMAP()

    # extract posterior samples
    stan_extract = vi_estimator.fit(
        stan_model_name=stan_model_name,
        model_param_names=model_param_names,
        data_input=data_input
    )

    expected_extract_keys = model_param_names[:]

    assert set(expected_extract_keys) == set(stan_extract.keys())
