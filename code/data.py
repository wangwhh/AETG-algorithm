class Data:
    def __init__(self, name, options, parameters, data):
        self.name = name
        self.options = options
        self.parameters = parameters
        self.data = data
        

def jingdong():
    options = ['品牌', '能效等级', 'SSD', '厚度', '机身材质', '屏幕尺寸', '刷新率']
    # 品牌
    brand = ['ThinkPad', 'DELL', '华为', 'Lenovo', 'Apple', 'hp', 'ASUS', 'MI', 'HONOR']
    # 能效等级
    energy_efficiency = ['一级', '二级', '三级']
    # SSD
    ssd = ['3TB', '128GB', '256GB+1TB', '512GB+2TB', '3TB*2']
    # 厚度
    thickness = ['15.0mm及以下', '15.1-18.0mm', '18.1-20.0mm', '20.0mm以上']
    # 机身材质
    body_material = ['金属', '金属+复合材质', '复合材质', '含碳纤维']
    # 屏幕尺寸
    screen_size = ['13.0英寸以下', '13.0-13.9英寸', '14.0-14.9英寸', '15.0-15.9英寸', '16.0-16.9英寸']
    # 刷新率
    refresh_rate = ['144Hz', '60Hz', '120Hz', '90Hz', '165Hz']
    
    parameters = [len(brand), len(energy_efficiency), len(ssd), len(thickness), len(body_material), len(screen_size), len(refresh_rate)]
    data = [brand, energy_efficiency, ssd, thickness, body_material, screen_size, refresh_rate]
    return Data('京东', options, parameters, data)

def xiecheng():
    options = ['票型', '出发地', '目的地', '仅看直飞', '舱型', '乘客类型']
    # 票型
    ticket_type = ['单程', '往返', '多程']
    # 出发地
    start = ['国内', '国际·中国港澳台热门', '亚洲', '欧洲', '美洲', '非洲', '大洋洲']
    # 目的地
    end = ['国内', '国际·中国港澳台热门', '亚洲', '欧洲', '美洲', '非洲', '大洋洲']
    # 仅看直飞
    direct = ['是', '否']
    # 舱型
    cabin_type = ['经济/超经舱', '公务/头等舱', '公务舱', '头等舱']
    # 乘客类型
    customer = ['仅成人', '成人与儿童', '成人与婴儿', '成人与儿童与婴儿']

    parameters = [len(ticket_type), len(start), len(end), len(direct), len(cabin_type), len(customer)]
    data = [ticket_type, start, end, direct, cabin_type, customer]
    return Data('携程', options, parameters, data)

