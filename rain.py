#!/usr/bin/env python3
"""
ASCII Art Rain Animation
A simple terminal animation showing rain drops falling from the sky.
"""

import random
import time
import sys
import os

def clear_screen():
    """Clear the terminal screen using ANSI escape codes."""
    print('\033[2J\033[H', end='', flush=True)

def get_terminal_size():
    """Get terminal dimensions."""
    try:
        size = os.get_terminal_size()
        return size.columns, size.lines
    except (OSError, ValueError):
        return 80, 24  # Default fallback size

class RainDrop:
    """Represents a single rain drop."""
    
    def __init__(self, width, height):
        self.x = random.randint(0, width - 1)
        self.y = random.randint(-height, 0)
        self.speed = random.uniform(0.5, 1.5)
        self.char = random.choice(['|', ':', '!', '.', '\''])
        
    def update(self):
        """Update drop position."""
        self.y += self.speed
        
    def is_offscreen(self, height):
        """Check if drop has fallen off screen."""
        return self.y >= height

def create_rain_frame(drops, width, height):
    """Create a single frame of the rain animation."""
    # Initialize empty grid
    grid = [[' ' for _ in range(width)] for _ in range(height)]
    
    # Place drops in grid
    for drop in drops:
        x = int(drop.x)
        y = int(drop.y)
        if 0 <= y < height and 0 <= x < width:
            grid[y][x] = drop.char
    
    # Convert grid to string
    frame = '\n'.join(''.join(row) for row in grid)
    return frame

def run_rain(duration=None, num_drops=50):
    """
    Run the ASCII rain animation.
    
    Args:
        duration: How long to run in seconds (None = infinite)
        num_drops: Number of rain drops to show
    """
    width, height = get_terminal_size()
    drops = [RainDrop(width, height) for _ in range(num_drops)]
    
    start_time = time.time()
    
    try:
        while True:
            # Check if duration has elapsed
            if duration and (time.time() - start_time) >= duration:
                break
            
            # Update all drops
            for drop in drops:
                drop.update()
                
                # Reset drop if it's offscreen
                if drop.is_offscreen(height):
                    drop.y = random.randint(-5, 0)
                    drop.x = random.randint(0, width - 1)
            
            # Create and display frame
            clear_screen()
            frame = create_rain_frame(drops, width, height)
            print(frame, end='', flush=True)
            
            # Control animation speed
            time.sleep(0.05)
            
    except KeyboardInterrupt:
        clear_screen()
        print("\nRain stopped!")
        sys.exit(0)

def main():
    """Main entry point."""
    print("ASCII Art Rain Animation")
    print("Press Ctrl+C to stop")
    print()
    time.sleep(2)
    
    # Run the rain animation
    run_rain()

if __name__ == '__main__':
    main()
