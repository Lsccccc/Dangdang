judge_rule={
    #玩家 VS 系统 等级：<=>
    
    #基本 VS 基本
    ("basic","basic"):"NNN",
    #基本 VS 攻击
    ("basic","attack"):"FFF",
    #基本 VS 防御
    ("basic","defense"):"NNN",
    #基本 VS 转换
    ("basic","exchange"):"NNN",
    #基本 VS 自杀
    ("basic","suicide"):"TTT",
    #基本 VS 升级
    ("basic","upgrade"):"NNN",
    #攻击 VS 基本
    ("attack","basic"):"TTT",
    #攻击 VS 攻击
    ("attack","attack"):"FNT",
    #攻击 VS 防御
    ("attack","defense"):"NNT",
    #攻击 VS 转换
    ("attack","exchange"):"FFT",
    #攻击 VS 自杀
    ("attack","suicide"):"TTT",
    #攻击 VS 升级
    ("attack","upgrade"):"TTT",
    #防御 VS 基本
    ("defense","basic"):"NNN",
    #防御 VS 攻击
    ("defense","attack"):"FNN",
    #防御 VS 防御
    ("defense","defense"):"NNN",
    #防御 VS 转换
    ("defense","exchange"):"NNN",
    #防御 VS 自杀
    ("defense","suicide"):"TTT",
    #防御 VS 升级
    ("defense","upgrade"):"NNN",
    #转换 VS 基本
    ("exchange","basic"):"NNN",
    #转换 VS 攻击
    ("exchange","attack"):"FTT",
    #转换 VS 防御
    ("exchange","defense"):"NNN",
    #转换 VS 转换
    ("exchange","exchange"):"NNN",
    #转换 VS 自杀
    ("exchange","suicide"):"FFF",
    #转换 VS 升级
    ("exchange","upgrade"):"NNN",
    #自杀 VS 基本
    ("suicide","basic"):"FFF",
    #自杀 VS 攻击
    ("suicide","attack"):"FFF",
    #自杀 VS 防御
    ("suicide","defense"):"FFF",
    #自杀 VS 转换
    ("suicide","exchange"):"TTT",
    #自杀 VS 自杀
    ("suicide","suicide"):"NNN",
    #自杀 VS 升级
    ("suicide","upgrade"):"FFF",
    #升级 VS 基本
    ("upgrade","basic"):"NNN",
    #升级 VS 攻击
    ("upgrade","attack"):"FFF",
    #升级 VS 防御
    ("upgrade","defense"):"NNN",
    #升级 VS 转换
    ("upgrade","exchange"):"NNN",
    #升级 VS 自杀
    ("upgrade","suicide"):"TTT",
    #升级 VS 升级
    ("upgrade","upgrade"):"NNN",
    }
