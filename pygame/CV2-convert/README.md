

## Convert from PyGame to CV2 and from CV2 to PyGame

You have to convert from `RGB` to `BGR` which is used in `CV2`.  
You have to `transpose` image - swap `width` with `height`.

```python
# --- move from PyGame to CV2 ---

cv2_image = pygame.surfarray.array3d(pygame_image)

cv2_image = cv2.transpose(cv2_image)
cv2_image = cv2.cvtColor(cv2_image, cv2.COLOR_RGB2BGR)

# --- move back from CV2 to PyGame ---

cv2_image = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB)
cv2_image = cv2.transpose(cv2_image)

pygame_image = pygame.surfarray.make_surface(cv2_image)
```
