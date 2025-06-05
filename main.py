from telegram_config import listar_canais, baixar_videos_por_id

def main():
    listar_canais()
    channel_id = input("\nEnter the channel ID: ")
    try:
        baixar_videos_por_id(int(channel_id))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

