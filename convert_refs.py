from __future__ import annotations

from pathlib import Path

from PIL import Image


def main() -> None:
    srcs = [
        r"C:\Users\lixue\.cursor\projects\d-cursor-test\assets\c__Users_lixue_AppData_Roaming_Cursor_User_workspaceStorage_9bd5c6f6d7ffdc907ca2b2ec5c6bbb0e_images______20260204225502_344_132-5cb1188b-b0b0-44c5-aa92-11e191242478.png",
        r"C:\Users\lixue\.cursor\projects\d-cursor-test\assets\c__Users_lixue_AppData_Roaming_Cursor_User_workspaceStorage_9bd5c6f6d7ffdc907ca2b2ec5c6bbb0e_images_Generated_Image_March_16__2026_-_9_28AM-c4b8b275-0d82-4929-afd3-63d70d70e7d7.png",
        r"C:\Users\lixue\.cursor\projects\d-cursor-test\assets\c__Users_lixue_AppData_Roaming_Cursor_User_workspaceStorage_9bd5c6f6d7ffdc907ca2b2ec5c6bbb0e_images_Generated_Image_March_16__2026_-_9_27AM-2e09c667-10e7-456e-ac76-d40d057fae95.png",
    ]

    dst_dir = Path(r"C:\Users\lixue\.cursor\projects\d-cursor-test\assets\converted")
    dst_dir.mkdir(parents=True, exist_ok=True)

    out: list[str] = []
    for i, p in enumerate(srcs, 1):
        img = Image.open(p)
        img.load()
        img = img.convert("RGBA")
        dst = dst_dir / f"ref_{i}.png"
        img.save(dst, format="PNG", optimize=False)
        out.append(str(dst))

    print("\n".join(out))


if __name__ == "__main__":
    main()

