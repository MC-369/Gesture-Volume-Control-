# Gesture-Volume-Control-
Gesture-Based Volume Control using OpenCV & MediaPipe

I developed a real-time hand gesture volume controller using Python that allows users to adjust system volume with intuitive hand movements — no physical interaction with keyboard or mouse required.

👨‍💻 What It Does
By tracking the distance between the thumb and index finger, the system dynamically maps that gesture to the system’s audio volume. Bringing the fingers close together mutes or lowers the volume, while spreading them apart increases it — just like pinching and zooming, but for sound!

🔧 Tech Stack & Tools Used:

🖐️ MediaPipe (Google) – Leveraged its hand landmark detection module to track 21 key points on the hand in real-time with high accuracy.
🎥 OpenCV – Captured webcam input, handled image processing, and displayed interactive feedback including FPS and volume level overlay.
🔊 pycaw + VB-Audio Virtual Cable – Controlled the system audio programmatically through COM interfaces, allowing seamless volume changes.
⚙️ Custom HandTracking Module – Built a reusable Python class that abstracts MediaPipe logic for hand detection, landmark extraction, finger distance calculation, and more.
📹 OBS Studio – Used for recording the live demo with synchronized real-time volume feedback, showing the direct effect of hand gestures.

📐 How It Works:

Webcam Feed is processed in real-time using OpenCV.

MediaPipe detects hand landmarks, especially the thumb tip and index finger tip.

The Euclidean distance between those two points is computed.

That distance is mapped to a volume level (e.g., 20px = 0%, 150px = 100%).

System volume is adjusted live using pycaw.

Visual UI overlays like a volume bar, gesture lines, and FPS counter enhance the user experience.

🧪 Additional Features:

Real-time FPS monitoring for performance insight.

Visual feedback like gesture lines and bounding boxes around detected hands.

Failsafes to handle cases when hand landmarks are lost or misread.

