

def H_model(CF_0, g_s, g_l, t, discount_rate):
    H = t / 2
    numerator = ( 1 + g_l ) + ( H * (g_s - g_l) )
    denominator = discount_rate - g_l
    return CF_0 * ( numerator / denominator )

def two_stage(CF_0, g_s, g_l, discount_rate, t):
    CF_list = [CF_0 * ( (1 + g_s) ** i) for i in range(1, t + 1)]
    discounted_cash_flows = [
        cf / (1 + discount_rate) ** (n + 1) for n, cf in enumerate(CF_list)
    ]
    terminal_value = (
                CF_0 * ( (1 + g_s) ** t ) * (1 + g_l)
            ) / (discount_rate - g_l)
    discounted_terminal_value = terminal_value / ( (1 + discount_rate) ** t)
    return sum(discounted_cash_flows) + discounted_terminal_value
