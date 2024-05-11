# deglazer

program to remove glaze / nightshade / glaze2 from images

## requirements
```
pip install -r requirements.txt
```

## usage
```
python run.py -h

python run.py clean image.png

python run.py clean_folder path/to/images --newfolder path/to/cleaned/images
```

## methods
- vaeloop
```diff
+ most consistent
~ passes image through VAE, which removes imperfections (e.g. glaze)
~ resizes images to a mult of 8
- needs a gpu
```
- glaze1
```diff
~ classical glaze remover (has it even worked at all?)
```
- glaze2
```diff
+ both vaeloop and glaze1 combined
~ passes image through VAE, which removes imperfections (e.g. glaze)
~ resizes images to a mult of 8
- needs a gpu
```

## effectiveness

considering that glaze/nightshade doesnt work at all, this is extremely effective (100% captioning accuracy after deglazing)

training effectiveness decreases after deglazing since glaze actually helps training (the glaze/shade acts as noise offset)

## faq

#### what does glaze *actually* do?
basically nothing; it adds adversarial noise which supposedly makes the model think a dog is a cat

the issue is SD doesnt really care about that since we pass it through a VAE, but it does confuse the CLIP (see: nightshade)

vaeloop will fix the 'glaze' and make it CLIP taggable (even though most people dont use CLIP)

#### why did you make this
glaze n co think that they've made a miracle cure for ai training on other art; they have not

#### is it possible to actually make images untrainable
not without making it terrible to watch/private

pick 2 of 3 things:
- untrainable
- good to watch
- publicly viewable
