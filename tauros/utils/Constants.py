from enum import Enum
import tauros.proto.WAMessage as WAProto


class MimeType(Enum):
    jpeg: str = "image/jpeg"
    png: str = "image/png"
    mp4: str = "video/mp4"
    gif: str = "video/gif"
    pdf: str = "application/pdf"
    ogg: str = "audio/ogg; codecs=opus"
    mp4Audio: str = "audio/mp4"
    ## For Stickers
    webp: str = "image/webp"
