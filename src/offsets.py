from dataclasses import dataclass

@dataclass
class Offsets:
    base_address: int = 0x2A4B4B8
    hp_current: int = 0x290
    hp_max: int = 0x294
    atk: int = 0x298
    def_: int = 0x29C
    magic: int = 0x2A0
    gold: int = 0x2B8
    inventory_ptr: int = 0x2D8
    battle_flag: int = 0x310
    timer: int = 0x328
    items_base: int = 0x2A4B5A8

CURRENT_OFFSETS = Offsets()
