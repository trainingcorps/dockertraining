# Stage 1: Build the Go app
FROM java-11 AS builder 

WORKDIR /app
COPY main.go .
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o server main.go #op1.jar 
#--------------------Artifact will carried to stage 2------------------------
# Stage 2: Minimal image
FROM scratch
COPY --from=builder /app/server /server
EXPOSE 8080
ENTRYPOINT ["/server"]