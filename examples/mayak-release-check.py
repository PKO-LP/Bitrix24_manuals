"""Проверка двух функций из урока 19."""

import importlib.util
from pathlib import Path


def main():
    path = Path(__file__).with_name("mayak_release.py")
    if not path.is_file():
        raise SystemExit("Сохраните свою работу как mayak_release.py рядом с этим файлом.")

    spec = importlib.util.spec_from_file_location("mayak_release", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    checks = [
        ("build_delivery_label", "Маяк | 2 кресла"),
        ("build_release_note", "Релиз 1.0: готово к проверке"),
    ]
    passed = True
    for name, expected in checks:
        function = getattr(module, name, None)
        if not callable(function):
            print(f"НЕ ПРОЙДЕНО: функция {name} отсутствует.")
            passed = False
            continue
        try:
            actual = function()
        except Exception as error:
            print(f"НЕ ПРОЙДЕНО: {name}: {error}")
            passed = False
            continue
        if actual == expected:
            print(f"ПРОЙДЕНО: {name}")
        else:
            print(f"НЕ ПРОЙДЕНО: {name}. Ожидалось {expected!r}, получено {actual!r}.")
            passed = False

    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
