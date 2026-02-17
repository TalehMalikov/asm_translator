from asm_translator.asm_translator import ASMTranslator

if __name__ == '__main__':
    test_files = [
        'data/add/Add.asm',
        'data/max/Max.asm',
        'data/max/MaxL.asm',
        'data/pong/Pong.asm',
        'data/pong/PongL.asm',
        'data/rect/Rect.asm',
        'data/rect/RectL.asm',
    ]

    for f in test_files:
        print(f"Translating {f}...")
        translator = ASMTranslator(f)
        translator.translate()
        print(f"Done!")