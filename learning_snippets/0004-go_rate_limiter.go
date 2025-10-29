package main

import (
    "context"
    "fmt"
    "time"
)

// Tiny token-bucket style limiter demo: allow 3 events per second
func main() {
    ctx := context.Background()
    ticker := time.NewTicker(333 * time.Millisecond) // ~3 tokens/sec
    defer ticker.Stop()

    tokens := make(chan struct{}, 3)

    // refill goroutine
    go func() {
        for {
            select {
            case <-ctx.Done():
                return
            case <-ticker.C:
                select {
                case tokens <- struct{}{}:
                default:
                }
            }
        }
    }()

    // simulate 10 requests and show when they're allowed
    for i := 1; i <= 10; i++ {
        <-tokens // block until a token available
        fmt.Printf("allowed request %d at %s\n", i, time.Now().Format(time.RFC3339Nano))
    }
}
