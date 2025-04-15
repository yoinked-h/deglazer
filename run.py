from pathlib import Path
import typer
import cv2
import numpy as np

app = typer.Typer()

@app.command()
def clean(image: Path, method='glaze1', newname='cleaned.png'):
    match method:
        case 'vaeloop':
            print('vae-related ones dont work; my bad')
            from methods.vaeloop import clean
        case 'glaze1':
            from methods.glaze1 import clean
        case 'glaze2':
            print('vae-related ones dont work; my bad')
            from methods.glaze2 import clean
        case _:
            from methods.glaze1 import clean # default
    base = cv2.imread(str(image)).astype(np.float32)
    cv2.imwrite(newname, clean(base).clip(0, 255).astype(np.uint8))
    return 0

@app.command()
def clean_folder(path: Path, method='glaze1', newfolder='output'):
    match method:
        case 'vaeloop':
            print('vae-related ones dont work; my bad')
            from methods.vaeloop import clean
        case 'glaze1':
            from methods.glaze1 import clean
        case 'glaze2':
            print('vae-related ones dont work; my bad')
            from methods.glaze2 import clean
        case _:
            from methods.glaze1 import clean # default
    for image in path.glob('*.png'):
        base = cv2.imread(str(image)).astype(np.float32)
        cv2.imwrite(str(Path(newfolder) / image.name), clean(base).clip(0, 255).astype(np.uint8))
    return 0
if __name__ == "__main__":
    app()
