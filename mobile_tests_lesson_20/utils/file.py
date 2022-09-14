def abs_path_from_project(relative_path: str):
    import mobile_tests_lesson_20
    from pathlib import Path

    return (
        Path(mobile_tests_lesson_20.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
