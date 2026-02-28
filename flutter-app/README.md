# Lao Knowledge Hub - Flutter App

## Quick Start

### Prerequisites

1. **Install Flutter** (3.16 or later)
   ```bash
   # Check installation
   flutter doctor
   ```

2. **Install Dependencies**
   ```bash
   cd flutter-app
   flutter pub get
   ```

3. **Configure Environment**
   Edit `lib/config/constants.dart`:
   ```dart
   const String apiUrl = 'http://localhost:8000/api/v1';
   const String supabaseUrl = 'https://your-project.supabase.co';
   const String supabaseAnonKey = 'your-anon-key';
   ```

### Run the App

```bash
# Run on Chrome (web)
flutter run -d chrome

# Run on Android emulator
flutter run -d android

# Run on iOS simulator (macOS only)
flutter run -d ios
```

## Project Structure

```
flutter-app/
├── lib/
│   ├── main.dart              # App entry point
│   ├── config/
│   │   ├── constants.dart     # App constants
│   │   ├── theme.dart         # App theme
│   │   └── routes.dart        # App routes
│   ├── models/
│   │   ├── book.dart          # Book model
│   │   ├── user.dart          # User model
│   │   ├── order.dart         # Order model
│   │   └── annotation.dart    # Annotation model
│   ├── services/
│   │   ├── auth_service.dart  # Authentication
│   │   ├── api_service.dart   # API client
│   │   └── storage_service.dart # Local storage
│   ├── providers/
│   │   ├── auth_provider.dart # Auth state
│   │   ├── book_provider.dart # Book state
│   │   └── cart_provider.dart # Cart state
│   ├── screens/
│   │   ├── home/              # Home screen
│   │   ├── browse/            # Browse screen
│   │   ├── book_detail/       # Book detail
│   │   ├── reader/            # PDF reader
│   │   ├── library/           # User library
│   │   ├── auth/              # Login/Register
│   │   └── profile/           # User profile
│   └── widgets/
│       ├── book_card.dart     # Book card widget
│       ├── search_bar.dart    # Search widget
│       └── reader/            # Reader widgets
├── test/
├── pubspec.yaml
└── README.md
```

## Features

### P0 (MVP)
- ✅ Browse books without login
- ✅ Book detail page
- ✅ User authentication
- ✅ PDF reader
- ✅ Annotations (highlight, notes)
- ✅ Shopping cart
- ✅ Reading progress sync

### P1 (Post-MVP)
- ⏳ Reviews & ratings
- ⏳ University/course filters
- ⏳ Rental option
- ⏳ Annotation export

## Testing

```bash
# Run tests
flutter test

# Run with coverage
flutter test --coverage
```

## Building for Production

### Web
```bash
flutter build web --release
```

### Android
```bash
flutter build apk --release
# or
flutter build appbundle --release
```

### iOS
```bash
flutter build ios --release
```

## Troubleshooting

### Package conflicts
```bash
flutter clean
flutter pub get
```

### Build errors
```bash
# Check Flutter installation
flutter doctor

# Update Flutter
flutter upgrade
```
