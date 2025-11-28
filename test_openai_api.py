#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test OpenAI API endpoint"""

import requests
import json

# API Configuration
API_BASE = "https://per.alisttr.top/v1"
API_KEY = "Trung6689@"

def test_openai_api():
    """Test OpenAI API translation"""
    url = f"{API_BASE}/chat/completions"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": "Translate to Vietnamese: Hello, this is a test message for TrendRadar project"
            }
        ],
        "temperature": 0.3
    }
    
    print("Testing OpenAI API endpoint...")
    print(f"URL: {url}")
    print(f"Payload: {json.dumps(payload, indent=2)}\n")
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        
        result = response.json()
        print("✓ API Response successful!")
        print(f"Status Code: {response.status_code}")
        print(f"\nResponse:\n{json.dumps(result, indent=2, ensure_ascii=False)}")
        
        # Extract translation
        if "choices" in result and len(result["choices"]) > 0:
            translation = result["choices"][0]["message"]["content"]
            print(f"\n✓ Translation: {translation}")
            return True, translation
        else:
            print("\n✗ No translation in response")
            return False, None
            
    except requests.exceptions.RequestException as e:
        print(f"\n✗ API Request failed: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response status: {e.response.status_code}")
            print(f"Response body: {e.response.text}")
        return False, None
    except Exception as e:
        print(f"\n✗ Error: {e}")
        return False, None

if __name__ == "__main__":
    success, translation = test_openai_api()
    if success:
        print("\n✓ OpenAI API is working correctly!")
    else:
        print("\n✗ OpenAI API test failed!")
    exit(0 if success else 1)
