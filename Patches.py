AP_SAVE_LOAD = {
    # ignore cheats
    0xb63c0: 0x60000000,  # nop

    # inject write function
    0xcebdc: 0x481dcb29,  # bl   -> 0x8028F204 (write function)

    # inject read function
    0xcf034: 0x481dc711,  # bl   -> 0x8028f244 (read function)

    # write function
    0x2ab8e4: 0x9421fff0,  # stwu sp, -0x0010 (sp)
    0x2ab8e8: 0x7c0802a6,  # mflr r0
    0x2ab8ec: 0x90010014,  # stw  r0, 0x0014 (sp)
    0x2ab8f0: 0x4bdb3dfd,  # bl   ->0x8004300C (Write_b1__7xSerialFi)
    0x2ab8f4: 0x3dc0817f,  # lis	r14, 0x817f
    0x2ab8f8: 0x39e00000,  # li   r15, 0
    0x2ab8fc: 0x7fe3fb78,  # mr	r3, r31
    0x2ab900: 0x7c8e782e,  # lwzx	r4, r14, r15
    0x2ab904: 0x4bdb3ed9,  # bl	->0x800430FC (Write__7xSerialFi)
    0x2ab908: 0x39ef0004,  # addi r15, r15, 4
    0x2ab90c: 0x2C0f007c,  # cmp  r15, 0x7c
    0x2ab910: 0x4081ffec,  # ble -> 0x8028f21c (-5)
    0x2ab914: 0x80010014,  # lwz	r0, 0x0014 (sp)
    0x2ab918: 0x7c0803a6,  # mtlr	r0
    0x2ab91c: 0x38210010,  # addi	sp, sp, 16
    0x2ab920: 0x4e800020,  # blr

    # read function
    0x2ab924: 0x9421fff0,  # stwu	sp, -0x0010 (sp)
    0x2ab928: 0x7c0802a6,  # mflr	r0
    0x2ab92c: 0x90010014,  # stw	r0, 0x0014 (sp)
    0x2ab930: 0x3dc0817f,  # lis	r14, 0x817f
    0x2ab934: 0x39e00000,  # li   r15, 0
    0x2ab938: 0x7fe3fb78,  # mr	r3, r31
    0x2ab93c: 0x7c8e7a14,  # add  r4, r14, r15
    0x2ab940: 0x7c9d2378,  # mr	r29, r4
    0x2ab944: 0x4bdb4111,  # bl	->0x80043374 (Read_7xSerialFPUi)
    0x2ab948: 0x39ef0004,  # addi r15, r15, 4
    0x2ab94c: 0x2C0f007c,  # cmp r15, 0x7c
    0x2ab950: 0x4081ffe8,  # ble -> 0x8028f258 (-6)
    0x2ab954: 0x3c80803c,  # lis	r4, 0x803C
    0x2ab958: 0x7fe3fb78,  # mr	r3, r31
    0x2ab95c: 0x38840558,  # addi	r4, r4, 1368
    0x2ab960: 0x3ba41738,  # addi	r29, r4, 5944
    0x2ab964: 0x7fa4eb78,  # mr	r4, r29
    0x2ab968: 0x4bdb40ed,  # bl	->0x80043374 (Read_7xSerialFPUi)
    0x2ab96c: 0x80010014,  # lwz	r0, 0x0014 (sp)
    0x2ab970: 0x7c0803a6,  # mtlr	r0
    0x2ab974: 0x38210010,  # addi	sp, sp, 16
    0x2ab978: 0x4e800020,  # blr

    # nuke remaining cheats info
    0x2AB980: bytes([0] * 0x17c)
}

SPATS_REWARD_FIX = {
    0x7fcd4: 0x60000000,  # nop
    0x7fcd8: 0x60000000,  # nop
    0x7fcdc: 0x60000000,  # nop
}

SOCKS_REWARD_FIX = {
    0x92ff8: 0x4080003c
}

GOLDEN_UNDERWEAR_REWARD_FIX = {
    0x7fd20: 0x80041738
}

LVL_ITEM_REWARD_FIX = {
    0x7fdcc: 0x60000000,  # nop
    0x7fdd0: 0x60000000,  # nop
    0x7fdd4: 0x60000000  # nop
}
