from ..write_labels import process_labels


def test_process_labels():
    key = 'mk'
    observations = [{key: 'A'}, {key: 'B'}, {key: 'A'}, {key: 'C'},
                    {key: 'C'}]
    config = process_labels(observations, 'mk')
    expected_labels = ['A', 'B', 'C']
    assert 'labels' in config
    for label in config['labels']:
        assert label['value'] in expected_labels

    observations = []
    config = process_labels(observations, 'mk')
    assert 'labels' in config
    assert len(config['labels']) == 0
