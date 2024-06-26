from torchvision import models
from torch import nn

def get_img_enc(args):
    if args.imgenc == 'base':
        pass
    elif args.imgenc == 'resnet18':
        model = models.resnet18(weights = 'IMAGENET1K_V1' if args.w else None)
        model.fc = nn.BatchNorm1d(512)
    else:
        raise ValueError(f"Model {args.imgenc} is not supported")

    return model