import cv2

def save_result(results, output_path):
    annotated = results[0].plot()
    cv2.imwrite(output_path, annotated)
