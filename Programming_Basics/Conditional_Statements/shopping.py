budget = float(input())
n_video_card = int(input())
m_processor = int(input())
p_memory_frame = int(input())

video_card_price = n_video_card * 250
processor_price = video_card_price * 0.35 * m_processor
memory_frame_price = video_card_price * 0.10 * p_memory_frame

final_price = video_card_price + processor_price + memory_frame_price

if n_video_card > m_processor:
    final_price = final_price * 0.85

if budget >= final_price:
    print(f"You have {budget - final_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {abs(budget - final_price):.2f} leva more!")
