import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './features/home/home.component';
import { ProfileComponent } from './features/profile/profile.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { MarketComponent } from './features/market/market.component';
import { SigninComponent } from './features/signin/signin.component';

@NgModule({
  declarations: [AppComponent],
  imports: [
    BrowserModule,
    NgbModule,
    AppRoutingModule,
    HomeComponent,
    ProfileComponent,
    MarketComponent,
    SigninComponent,
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
